"""Create dev-freebie relationship

Revision ID: cc50d79cf00b
Revises: 8b8cc2e88779
Create Date: 2024-01-07 11:15:40.538800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc50d79cf00b'
down_revision = '8b8cc2e88779'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dev_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_freebies_dev_id_devs'), 'devs', ['dev_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_freebies_dev_id_devs'), type_='foreignkey')
        batch_op.drop_column('dev_id')

    # ### end Alembic commands ###
